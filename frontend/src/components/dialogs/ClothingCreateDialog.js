import { Dialog, TextField, Button, MenuItem } from '@mui/material';

export default function ClothingCreateDialog() {
  const [open, setOpen] = useState(false);
  const [clothing, setClothing] = useState({
    type: '',
    color: '',
    size: ''
  });

  const handleSubmit = async () => {
    try {
      await WardrobeAPI.getAPI().createClothing(clothing);
      setOpen(false);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Dialog open={open} onClose={() => setOpen(false)}>
      <TextField
        label="Typ"
        value={clothing.type}
        onChange={(e) => setClothing({...clothing, type: e.target.value})}
      />
      <TextField
        label="Farbe"
        value={clothing.color}
        onChange={(e) => setClothing({...clothing, color: e.target.value})}
      />
      <Button onClick={handleSubmit}>Speichern</Button>
    </Dialog>
  );
}