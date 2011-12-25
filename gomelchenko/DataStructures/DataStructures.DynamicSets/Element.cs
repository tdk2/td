namespace DataStructures.DynamicSets
{
    /// <summary>
    /// Represent an element in a dynamic set
    /// </summary>
    /// <typeparam name="TKey">The type of the key.</typeparam>
    /// <typeparam name="TData">The type of the data.</typeparam>
    public class Element<TKey, TData>
    {
        public TKey Key { get; protected set; }

        public TData Data { get; protected set; }
    }
}
