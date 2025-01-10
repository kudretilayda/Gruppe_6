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
  
  const [newOutfit, setNewOutfit] = useState({
    outfit_name: '',
    items: [],
    style: null,
  });

  // Lade Styles und Outfits beim Start
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
    if (selectedStyle) {
      setCurrentStep(2);
    }
  };

  const handleTabChange = (event, newValue) => {
    setSelectedTab(newValue);
    setCurrentStep(1);
    setSelectedStyle('');
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
    </div>
  );
};

export default Outfits;