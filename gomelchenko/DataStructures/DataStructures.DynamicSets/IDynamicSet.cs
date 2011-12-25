using System;

namespace DataStructures.DynamicSets
{
    /// <summary>
    /// Represents a dynamic set
    /// </summary>
    /// <typeparam name="TKey">The type of the key.</typeparam>
    /// <typeparam name="TData">The type of the data.</typeparam>
    public interface IDynamicSet<TKey, TData>
    {
        #region Queries
        /// <summary>
        /// Searches the specified key.
        /// </summary>
        /// <param name="key">The key.</param>
        /// <returns>The element that has its key equal to provided one</returns>
        Element<TKey, TData> Search(TKey key);

        /// <summary>
        /// Minimums this instance.
        /// </summary>
        /// <returns>The minimum element</returns>
        Element<TKey, TData> Minimum();

        /// <summary>
        /// Maximums this instance.
        /// </summary>
        /// <returns>The maximum element</returns>
        Element<TKey, TData> Maximum();

        /// <summary>
        /// Successors this instance.
        /// </summary>
        /// <param name="element"></param>
        /// <returns>The element thta is a successor of provided on</returns>
        Element<TKey, TData> Successor(Element<TKey, TData> element);

        /// <summary>
        /// Predecessors this instance.
        /// </summary>
        /// <returns>The element thta is a successor of provided on</returns>
        Element<TKey, TData> Predecessor(); 

        #endregion

        #region Modifying operations

        /// <summary>
        /// Inserts the specified element.
        /// </summary>
        /// <param name="element">The element.</param>
        void Insert(Element<TKey, TData> element);

        /// <summary>
        /// Deletes the specified element.
        /// </summary>
        /// <param name="element">The element.</param>
        void Delete(Element<TKey, TData> element); 

        #endregion
    }
}
