using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using DataStructures.DynamicSets;

namespace BST
{
    class Program
    {
        static void Main(string[] args)
        {
            var tree = new BinarySearchTree<int, int>();
            //tree.Insert(new BinaryTreeNode<int, int>(5, 0));
            tree.Insert(new BinaryTreeNode<int, int>(7, 0));
            //tree.Insert(new BinaryTreeNode<int, int>(3, 0));

            tree.Insert(new BinaryTreeNode<int, int>(7, 1));
            tree.Insert(new BinaryTreeNode<int, int>(7, 2));
            tree.Insert(new BinaryTreeNode<int, int>(7, 3));
            tree.Insert(new BinaryTreeNode<int, int>(7, 4));
            tree.Insert(new BinaryTreeNode<int, int>(7, 5));
            tree.Insert(new BinaryTreeNode<int, int>(7, 6));
            PrintTree(tree);

            Console.ReadKey();
        }

        private static void PrintTree<TKey, TData>(BinarySearchTree<TKey, TData> tree) where TKey : IEquatable<TKey>, IComparable<TKey>
        {
            tree.IterateInOrder(node => Console.Write("({0} {1}){2}", node.Key, node.Data, " "));
            Console.WriteLine();
        }
    }
}