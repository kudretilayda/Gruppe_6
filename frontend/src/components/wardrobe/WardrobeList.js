import React from 'react';
import { List, ListItem, ListItemText, Divider } from '@mui/material';

const WardrobeList = ({ items }) => {
  return (
    <List>
      {items.map((item, index) => (
        <React.Fragment key={index}>
          <ListItem>
            <ListItemText
              primary={item.type}
              secondary={`Verwendung: ${item.usage}`}
            />
          </ListItem>
          {index < items.length - 1 && <Divider />} {/* Trennlinie zwischen Items */}
        </React.Fragment>
      ))}
    </List>
  );
};

export default WardrobeList;
