# Analysis-of-CuckooFilter

Analysis of CuckooFilter in comparison to BloomFilter on single node CPU, multiple node CPU, and single GPU


Task 1 : single node CPU
    1) Implement CuckooFilter and BloomFilter in non-parallel.

    2) Test simple performance on different number inputs in string
        - Time for addition of all item.
        - Time for retrieval item.
        - Memory Usage of each Filter.
        - Compare False positive rate
    3) Test complicated performance

        - Time of addition/retrieval depending on percentage of usage of hashtable.
        - False Positive rate depending on percentage of usage of hashtable.


Task 2 : multiple node CPU
    1) Implement CuckooFilter and Bloomfilter in Parallel.

    2) & 3) repeat of Task 1

    4) Compare performance on different number of nodes.

Task 3 : single node GPU
    repeat Task 1 on GPU setting

Task 4 : Report
    Make a solid conclusion based on the data from Task1, Task2, and Task3



