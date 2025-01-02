import React from 'react';
import { Card, CardContent, CardActions, Typography, Button, Grid } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import WardrobeIcon from '@mui/icons-material/Checkroom'; // Neues Icon für den Kleiderschrank
import StyleIcon from '@mui/icons-material/Style'; // Für Outfit-Stile
import { styled } from '@mui/system';

/**Optische Anpassungen zum digitalen Kleiderschrank */

const StyledCard = styled(Card)(({ theme, isAvailable }) => ({
  padding: theme.spacing(2),
  border: isAvailable ? '3px solid green' : '1px solid gray', // Randfarbe basierend auf Verfügbarkeit
  [theme.breakpoints.down('sm')]: {
    padding: theme.spacing(1),
  },
}));

const StyledIcon = styled('span')(({ theme }) => ({
  fontSize: 24,
  [theme.breakpoints.down('sm')]: {
    fontSize: 16,
  },
}));

const StyledButton = styled(Button)(({ theme }) => ({
  fontSize: 14,
  [theme.breakpoints.down('sm')]: {
    fontSize: 10,
  },
  display: 'flex',
  justifyContent: 'center',
  alignContent: "center"
}));

function WardrobeCard({ outfit, onEdit, onDelete, onViewOutfit, onWearOutfit, isAvailable }) {
  return (
    <StyledCard isAvailable={isAvailable}>
      <CardContent>
        <Typography variant="h5">{outfit.getTitle()}</Typography>
        <Typography color="textSecondary">
          Size: {outfit.getSize()} <br />
          Description: {outfit.getDescription()}
        </Typography>
      </CardContent>
      <CardActions>
        <Grid container spacing={1}>
          <Grid item xs={12} sm={6} md={3}>
            <StyledButton
              size="small"
              startIcon={<WardrobeIcon className={StyledIcon} />}
              onClick={() => onViewOutfit(outfit.getId())}
              fullWidth
            >
              Show <br /> details
            </StyledButton>
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <StyledButton
              size="small"
              startIcon={<EditIcon className={StyledIcon} />}
              onClick={() => onEdit(outfit)}
              fullWidth
            >
              Edit <br /> outfit
            </StyledButton>
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <StyledButton
              size="small"
              startIcon={<StyleIcon className={StyledIcon} />}
              onClick={() => onWearOutfit(outfit)}
              fullWidth
            >
              Wear <br /> outfit
            </StyledButton>
          </Grid>

          <Grid item xs={12} sm={6} md={3}>
            <StyledButton
              size="small"
              startIcon={<DeleteIcon className={StyledIcon} />}
              onClick={() => onDelete(outfit)}
              fullWidth
            >
              Delete
            </StyledButton>
          </Grid>
        </Grid>
      </CardActions>
    </StyledCard>
  );
}

export default WardrobeCard;
