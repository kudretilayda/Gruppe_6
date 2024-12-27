import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';

const WardrobeList = ({ items }) => {
  return (
    <List>
      {items.map((item, index) => (
        <ListItem key={index}>
          <ListItemText
            primary={item.type}
            secondary={`Verwendung: ${item.usage}`}
          />
        </ListItem>
      ))}
    </List>
  );
};

export default WardrobeList;