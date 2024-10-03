import pandas as pd
import suggests
from time import gmtime, strftime
from time import sleep


def main():
    queries = ['democrat',
     'democrats',
     'election',
     'election candidates',
     'election coverage',
     'election date',
     'election day',
     'election issues',
     'election news',
     'election polls',
     'election predictions',
     'election time',
     'election updates',
     'elections',
     'how to register',
     'how to register to vote',
     'how to vote',
     'local election',
     'poll results',
     'polls',
     'primaries',
     'realclearpolitics',
     'republican',
     'republicans',
     'sample ballot',
     'federal election',
     'voter registration',
     'voting',
     'voting locations',
     'when is the election',
     'where can I vote',
     'where do I vote',
     'where to vote',
     "who's running"]

    daily_pulls = []
    daily_suggests = []

       
    ## Iterating through each seed query, assigning a variable to the seed
    for seed in queries[0:1]:
        ## generating the suggests item
        s = suggests.get_suggests(seed, source='google')
        suggestion = {seed:s['suggests']}
        daily_suggests.append(suggestion)
        ## generating the tree from the suggests item
        tree = suggests.get_suggests_tree(seed,source='google')

        ## generating edges from the tree
        edges = suggests.to_edgelist(tree)

        ## generating the parents from the edges
        parents = suggests.add_parent_nodes(edges)

        ## generating the grandparents from the parents
        grandparents = parents.apply(suggests.add_metanodes,axis=1)
        ## appending the dataframe returned to a larger list of dataframes
        daily_pulls.append(grandparents)
        ## sleeping
        sleep(3)

    df = pd.concat(daily_pulls)

    curr_date = strftime("%Y-%m-%d", gmtime())
    print (curr_date)
    
    df.to_csv(f'{curr_date}-autocomplete.csv')


if __name__=="__main__":
    main()
