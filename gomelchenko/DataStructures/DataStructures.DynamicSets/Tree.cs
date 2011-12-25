using System;

namespace DataStructures.DynamicSets
{
    public abstract class Tree<TKey, TData> : IDynamicSet<TKey, TData> 
    {
        /// <summary>
        /// Searches the specified key.
        /// </summary>
        /// <param name="key">The key.</param>
        /// <returns>The element that has its key equal to provided one</returns>
        public abstract Element<TKey, TData> Search(TKey key);

        /// <summary>
        /// Inserts the specified element.
        /// </summary>
        /// <param name="element">The element.</param>
        public abstract void Insert(Element<TKey, TData> element);

        /// <summary>
        /// Deletes the specified element.
        /// </summary>
        /// <param name="element">The element.</param>
        public abstract void Delete(Element<TKey, TData> element);

        /// <summary>
        /// Minimums this instance.
        /// </summary>
        /// <returns>The minimum element</returns>
        public abstract Element<TKey, TData> Minimum();

        /// <summary>
        /// Maximums this instance.
        /// </summary>
        /// <returns>The maximum element</returns>
        public abstract Element<TKey, TData> Maximum();

        /// <summary>
        /// Successors this instance.
        /// </summary>
        /// <param name="element"></param>
        /// <returns>The element thta is a successor of provided on</returns>
        public abstract Element<TKey, TData> Successor(Element<TKey, TData> element);

        /// <summary>
        /// Predecessors this instance.
        /// </summary>
        /// <returns>The element thta is a successor of provided on</returns>
        public abstract Element<TKey, TData> Predecessor();
    }
}
