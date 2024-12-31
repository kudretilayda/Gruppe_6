export default function WardrobeManagement() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadClothingItems();
  }, []);

  async function loadClothingItems() {
    try {
      const data = await WardrobeAPI.getAPI().getClothingItems();
      setItems(data);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;

  return (
    <Grid container spacing={2}>
      {items.map(item => (
        <Grid item xs={12} sm={6} md={4} key={item.id}>
          <ClothingCard item={item} onDelete={loadClothingItems} />
        </Grid>
      ))}
      <ClothingCreateDialog />
    </Grid>
  );
}