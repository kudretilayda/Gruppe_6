import React from 'react';
import { List, ListItem, ListItemText } from '@material-ui/core';

const StyleList = ({ styles }) => {
  return (
    <List>
      {styles.map((style, index) => (
        <ListItem key={index}>
          <ListItemText
            primary={style.name}
            secondary={`Features: ${style.features.join(', ')}`}
          />
        </ListItem>
      ))}
    </List>
  );
};

export default StyleList;