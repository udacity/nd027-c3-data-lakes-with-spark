#TODO run this in jupyter notebook

from pyspark import SparkContext

sc = SparkContext('local[*]', 'pyspark')

my_dict = {"item1": 1, "item2": 2, "item3": 3, "item4": 4} 
my_list = ["item1", "item2", "item3", "item4"]

my_dict_bc = sc.broadcast(my_dict)

def my_func(letter):
    return my_dict_bc.value[letter] 

my_list_rdd = sc.parallelize(my_list)

result = my_list_rdd.map(lambda x: my_func(x)).collect()

print(result)
