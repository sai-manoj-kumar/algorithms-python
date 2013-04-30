__author__ = 'saimanoj'

import sieve
import ds.tree


def main():
    t = ds.tree.Tree('/')
    node = ds.tree.TreeNode('a')
    t.add(t.root, node)
    t.remove(node)
    print 'bye'


def sundaram_sieve_demo():
    primes = list(sieve.sundaram(10000))
    print len(primes)
    # print primes


if __name__ == "__main__":
    main()

