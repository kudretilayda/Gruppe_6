import React, { useState, useEffect } from 'react';
import {
  Typography, Grid, Card, CardContent, Button, Dialog,
  DialogTitle, DialogContent, DialogActions, TextField,
  Chip, CardActions, IconButton, Box, Select, MenuItem,
  FormControl, Paper, Tabs, Tab
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const TabPanel = ({ children, value, index }) => (
  <div hidden={value !== index}>
    {value === index && <Box p={3}>{children}</Box>}
  </div>
);

const ValidationSteps = ({ currentStep }) => {
  const steps = [
    { label: "Style auswählen", number: 1 },
    { label: "Kleidungsstücke auswählen", number: 2 },
    { label: "Outfit validieren lassen", number: 3 }
  ];

  return (
    <Box display="flex" mb={4} mt={2}>
      {steps.map((step, index) => (
        <Box key={step.number} display="flex" alignItems="center" mr={4}>
          <Box
            sx={{
              width: 24,
              height: 24,
              borderRadius: '50%',
              bgcolor: currentStep >= step.number ? 'primary.main' : 'grey.300',
              color: 'white',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              mr: 1
            }}
          >
            {step.number}
          </Box>
          <Typography color={currentStep >= step.number ? 'primary' : 'text.secondary'}>
            {step.label}
          </Typography>
        </Box>
      ))}
    </Box>
  );
};

const Outfits = ({ wardrobeItems = [] }) => {
  const [outfits, setOutfits] = useState([]);
  const [styles, setStyles] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentOutfitIndex, setCurrentOutfitIndex] = useState(null);
  const [selectedTab, setSelectedTab] = useState(0);
  const [currentStep, setCurrentStep] = useState(1);
  const [selectedStyle, setSelectedStyle] = useState('');
  const [selectedWardrobeItem, setSelectedWardrobeItem] = useState(null);
  const [filteredOutfits, setFilteredOutfits] = useState([]);

  const [newOutfit, setNewOutfit] = useState({
    outfit_name: '',
    items: [],
    style: null,
  });

  // Load Styles and Outfits on start
  useEffect(() => {
    const savedStyles = localStorage.getItem('styles');
    const savedOutfits = localStorage.getItem('outfits');

    if (savedStyles) {
      setStyles(JSON.parse(savedStyles));
    }
    if (savedOutfits) {
      setOutfits(JSON.parse(savedOutfits));
    }
  }, []);

  const handleStyleSelect = (e) => {
    const styleId = e.target.value;
    const selectedStyle = styles.find(style => style.name === styleId);
    setSelectedStyle(styleId);

    // If on the filter tab, filter outfits by style
    if (selectedTab === 2) {
      const filtered = outfits.filter(outfit => outfit.style === styleId);
      setFilteredOutfits(filtered);
    } else {
      if (selectedStyle) {
        setCurrentStep(2);
      }
    }
  };

  const handleWardrobeItemSelect = (item) => {
    setSelectedWardrobeItem(item);
    // Find outfits containing this specific item
    const filtered = outfits.filter(outfit =>
      outfit.items.some(itemId => itemId === item.id)
    );
    setFilteredOutfits(filtered);
    setCurrentStep(3);
  };

  const handleTabChange = (event, newValue) => {
    setSelectedTab(newValue);
    setCurrentStep(1);
    setSelectedStyle('');
    setSelectedWardrobeItem(null);
    setFilteredOutfits([]);
  };

  const saveOutfits = (updatedOutfits) => {
    setOutfits(updatedOutfits);
    localStorage.setItem('outfits', JSON.stringify(updatedOutfits));
  };

  const handleAddOutfit = () => {
    const updatedOutfits = [...outfits, { ...newOutfit, style: selectedStyle }];
    saveOutfits(updatedOutfits);
    setOpenDialog(false);
    setNewOutfit({ outfit_name: '', items: [], style: null });
  };

  const handleDeleteOutfit = (index) => {
    const updatedOutfits = outfits.filter((_, i) => i !== index);
    saveOutfits(updatedOutfits);
  };

  const renderFilteredOutfits = (filterList) => (
    <Grid container spacing={3}>
      {filterList.map((outfit, index) => (
        <Grid item xs={12} sm={6} md={4} key={index}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6">{outfit.outfit_name}</Typography>
              <Typography color="textSecondary" paragraph>
                Style: {outfit.style || 'Kein Style ausgewählt'}
              </Typography>
              <Box display="flex" flexWrap="wrap">
                {outfit.items.map((itemId, i) => (
                  <Chip
                    key={i}
                    label={wardrobeItems.find(item => item.id === itemId)?.item_name}
                    style={{
                      margin: '0.25rem',
                      backgroundColor: '#e0e0e0',
                      color: '#333',
                      borderRadius: '16px',
                    }}
                  />
                ))}
              </Box>
            </CardContent>
            <CardActions>
              <IconButton
                color="primary"
                onClick={() => {
                  setIsEditing(true);
                  setCurrentOutfitIndex(index);
                  setNewOutfit(outfit);
                  setOpenDialog(true);
                }}
              >
                <EditIcon />
              </IconButton>
              <IconButton
                color="secondary"
                onClick={() => handleDeleteOutfit(index)}
              >
                <DeleteIcon />
              </IconButton>
            </CardActions>
          </Card>
        </Grid>
      ))}
    </Grid>
  );

  return (
    <div className="p-4">
      <Paper sx={{ width: '100%', bgcolor: 'background.paper', mb: 4 }}>
        <Tabs
          value={selectedTab}
          onChange={handleTabChange}
          indicatorColor="primary"
          textColor="primary"
          variant="fullWidth"
        >
          <Tab label="OUTFIT NACH STYLE VALIDIEREN" />
          <Tab label="OUTFIT NACH WUNSCHKLEIDUNGSSTÜCK VALIDIEREN" />
          <Tab label="OUTFIT NACH STYLE FILTERN" />
        </Tabs>

        <TabPanel value={selectedTab} index={0}>
          <ValidationSteps currentStep={currentStep} />

          <FormControl fullWidth>
            <Select
              value={selectedStyle}
              onChange={handleStyleSelect}
              displayEmpty
              sx={{ mb: 2 }}
            >
              <MenuItem value="" disabled>
                Style auswählen
              </MenuItem>
              {styles.map((style, index) => (
                <MenuItem key={index} value={style.name}>
                  {style.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {selectedStyle && currentStep === 2 && (
            <Box mt={2}>
              <Typography variant="h6" gutterBottom>
                Gewählter Style: {selectedStyle}
              </Typography>
              <Typography variant="body1" gutterBottom>
                Features: {styles.find(s => s.name === selectedStyle)?.features.join(', ')}
              </Typography>

              <Button
                variant="contained"
                color="primary"
                onClick={() => setCurrentStep(3)}
                fullWidth
                sx={{ mt: 2 }}
              >
                Weiter zur Validierung
              </Button>
            </Box>
          )}

          {currentStep === 3 && (
            <Box mt={2}>
              <Typography variant="h6" gutterBottom>
                Outfit Validierung
              </Typography>
              {/* Hier können Sie die Validierungslogik implementieren */}
            </Box>
          )}
        </TabPanel>

        <TabPanel value={selectedTab} index={1}>
  <Typography variant="h6" gutterBottom>
    Wählen Sie ein Kleidungsstück aus Ihrem Kleiderschrank
  </Typography>
  <FormControl fullWidth>
    <Select
      value={selectedWardrobeItem?.id || ''}
      onChange={(e) => {
        const itemId = e.target.value;
        const selectedItem = wardrobeItems.find(item => item.id === itemId);
        handleWardrobeItemSelect(selectedItem);
      }}
      displayEmpty
    >
      <MenuItem value="" disabled>
        Kleidungsstück auswählen
      </MenuItem>
      {wardrobeItems.map((item) => (
        <MenuItem key={item.id} value={item.id}>
          {item.item_name}
        </MenuItem>
      ))}
    </Select>
  </FormControl>

  {selectedWardrobeItem && currentStep === 3 && (
    <Box mt={4}>
      <Typography variant="h6" gutterBottom>
        Outfits mit {selectedWardrobeItem.item_name}
      </Typography>
      {filteredOutfits.length > 0 ? (
        renderFilteredOutfits(filteredOutfits)
      ) : (
        <Typography color="textSecondary">
          Keine Outfits mit diesem Kleidungsstück gefunden.
        </Typography>
      )}
    </Box>
  )}
</TabPanel>


        <TabPanel value={selectedTab} index={2}>
          <Typography variant="h6" gutterBottom>
            Wählen Sie einen Style zum Filtern
          </Typography>
          <FormControl fullWidth>
            <Select
              value={selectedStyle}
              onChange={handleStyleSelect}
              displayEmpty
            >
              <MenuItem value="" disabled>
                Style auswählen
              </MenuItem>
              {styles.map((style, index) => (
                <MenuItem key={index} value={style.name}>
                  {style.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {selectedStyle && (
            <Box mt={4}>
              <Typography variant="h6" gutterBottom>
                Outfits im {selectedStyle} Style
              </Typography>
              {filteredOutfits.length > 0 ? (
                renderFilteredOutfits(filteredOutfits)
              ) : (
                <Typography color="textSecondary">
                  Keine Outfits in diesem Style gefunden.
                </Typography>
              )}
            </Box>
          )}
        </TabPanel>
      </Paper>

      {/* Outfit Liste */}
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Meine Outfits</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Outfit erstellen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {outfits.map((outfit, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h6">{outfit.outfit_name}</Typography>
                <Typography color="textSecondary" paragraph>
                  Style: {outfit.style || 'Kein Style ausgewählt'}
                </Typography>
                <Box display="flex" flexWrap="wrap">
                  {outfit.items.map((itemId, i) => (
                    <Chip
                      key={i}
                      label={wardrobeItems.find(item => item.id === itemId)?.item_name}
                      style={{
                        margin: '0.25rem',
                        backgroundColor: '#e0e0e0',
                        color: '#333',
                        borderRadius: '16px',
                      }}
                    />
                  ))}
                </Box>
              </CardContent>
              <CardActions>
                <IconButton
                  color="primary"
                  onClick={() => {
                    setIsEditing(true);
                    setCurrentOutfitIndex(index);
                    setNewOutfit(outfit);
                    setOpenDialog(true);
                  }}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  color="secondary"
                  onClick={() => handleDeleteOutfit(index)}
                >
                  <DeleteIcon />
                </IconButton>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* Dialog for creating/editing outfits */}
      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>{isEditing ? 'Outfit bearbeiten' : 'Neues Outfit erstellen'}</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Outfit Name"
            fullWidth
            value={newOutfit.outfit_name}
            onChange={(e) => setNewOutfit({...newOutfit, outfit_name: e.target.value})}
          />
          {/* You could add more fields here for selecting wardrobe items */}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)} color="primary">
            Abbrechen
          </Button>
          <Button onClick={handleAddOutfit} color="primary">
            Speichern
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Outfits;