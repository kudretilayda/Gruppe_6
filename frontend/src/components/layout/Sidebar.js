import React from 'react';
import { Drawer, List, ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import { Closet, Style, OutlinedFlag } from '@material-ui/icons';
import { useHistory } from 'react-router-dom';

export default function Sidebar() {
  const history = useHistory();

  const menuItems = [
    { text: 'Kleiderschrank', icon: <Closet />, path: '/kleiderschrank' },
    { text: 'Outfits', icon: <OutlinedFlag />, path: '/outfits' },
    { text: 'Styles', icon: <Style />, path: '/styles' }
  ];

  return (
    <Drawer variant="permanent">
      <List>
        {menuItems.map((item) => (
          <ListItem button key={item.text} onClick={() => history.push(item.path)}>
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}