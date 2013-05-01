__author__ = 'saimanoj'

import sieve
import ds.tree


def main():
    t = ds.tree.Tree('/')
    node_a = ds.tree.TreeNode('a')
    t.add(t.root, node_a)
    node_b = ds.tree.TreeNode('b')
    t.add(t.root, node_b)
    node_c = ds.tree.TreeNode('c')
    t.add(t.root, node_c)
    node_d = ds.tree.TreeNode('d')
    t.add(node_c, node_d)
    t.root.data = '//'
    # t.remove(node_d)
    t.get_all_nodes()
    print 'bye'


def sundaram_sieve_demo():
    primes = list(sieve.sundaram(10000))
    print len(primes)
    # print primes


if __name__ == "__main__":
    main()

