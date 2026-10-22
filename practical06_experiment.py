import numpy as np

# Reproducible demonstration instance (not an OR-Library dataset)
rng = np.random.default_rng(2026)
n=100
weights=rng.integers(1,31,size=n)
values=rng.integers(10,101,size=n)
capacity=int(weights.sum()*0.35)
M=10*values.max()

def fitness(pop):
    total_v=pop@values
    total_w=pop@weights
    return total_v-M*np.maximum(0,total_w-capacity)

def run(seed, tournament_size=3, crossover='two-point', mutation=0.02):
    rg=np.random.default_rng(seed)
    pop=(rg.random((150,n))<0.30).astype(np.int8)
    best_hist=[]; avg_hist=[]
    for gen in range(201):
        fs=fitness(pop)
        best_hist.append(int(fs.max())); avg_hist.append(float(fs.mean()))
        if gen==200: break
        elites=pop[np.argsort(fs)[-2:]].copy()
        children=[]
        while len(children)<148:
            ids=rg.integers(0,150,size=(2,tournament_size))
            p1,p2=pop[ids[np.arange(2),np.argmax(fs[ids],axis=1)]]
            a=p1.copy();b=p2.copy()
            if rg.random()<0.9:
                if crossover=='uniform':
                    mask=rg.random(n)<0.5
                    a=np.where(mask,p1,p2); b=np.where(mask,p2,p1)
                else:
                    x,y=sorted(rg.choice(np.arange(1,n),size=2,replace=False))
                    a[x:y]=p2[x:y]; b[x:y]=p1[x:y]
            a^=(rg.random(n)<mutation).astype(np.int8)
            b^=(rg.random(n)<mutation).astype(np.int8)
            children.extend([a,b])
        pop=np.vstack([elites,np.array(children[:148],dtype=np.int8)])
    ix=np.argmax(fitness(pop))
    sol=pop[ix]
    return {'best':int(best_hist[-1]),'weight':int(sol@weights),'value':int(sol@values),'best_history':best_hist,'average_history':avg_hist}

if __name__=='__main__':
    variants={'Baseline':{},'Tournament k=2':{'tournament_size':2},'Uniform crossover':{'crossover':'uniform'},'Mutation p=0.10':{'mutation':0.10}}
    print('n=',n,'capacity=',capacity,'M=',M,'total_weight=',sum(weights))
    import csv
    with open('/mnt/data/practical06_results.csv','w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['Variant','Seed','Best fitness','Weight','Value','Gen first reaches baseline median'])
        baseline=[run(s,**variants['Baseline']) for s in [42,43,44]]
        median=float(np.median([x['best'] for x in baseline]))
        import matplotlib.pyplot as plt
        plt.figure(figsize=(7.2,3.6))
        plt.plot(baseline[0]['best_history'],label='Best fitness')
        plt.plot(baseline[0]['average_history'],label='Average fitness')
        plt.xlabel('Generation');plt.ylabel('Fitness');plt.title('Baseline GA convergence (seed 42)')
        plt.legend();plt.grid(alpha=0.25);plt.tight_layout();plt.savefig('/mnt/data/practical06_convergence.png',dpi=175);plt.close()
        for name,params in variants.items():
            runs=baseline if name=='Baseline' else [run(s,**params) for s in [42,43,44]]
            vals=[r['best'] for r in runs]
            hit=[next((i for i,v in enumerate(r['best_history']) if v>=median),None) for r in runs]
            for seed,r,g in zip([42,43,44],runs,hit): wr.writerow([name,seed,r['best'],r['weight'],r['value'],g if g is not None else 'Not reached'])
            print(name,'values=',vals,'mean=',round(float(np.mean(vals)),1),'sd=',round(float(np.std(vals,ddof=1)),1),'gens=',hit,'sample_weight=',runs[0]['weight'])
