import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { AppBar, Toolbar, Typography, Tabs, Tab } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';
import ProfileDropDown from '../dialogs/ProfilDropDown.js';

class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tabindex: 0,
    };
  }

  handleTabChange = (event, newIndex) => {
    this.setState({ tabindex: newIndex });
  };

  render() {
    const { user } = this.props;

    return (
        <AppBar position="static" color="primary">
          <Toolbar>
            <Typography variant="h6" sx={{ flexGrow: 1 }} component={RouterLink} to={process.env.PUBLIC_URL + '/'}>
              Digital Wardrobe
            </Typography>
            {user && <ProfileDropDown user={user} />}
          </Toolbar>
          {user && (
              <Tabs
                  value={this.state.tabindex}
                  onChange={this.handleTabChange}
                  indicatorColor="secondary"
                  textColor="inherit"
                  centered
              >
                <Tab label="Wardrobe" component={RouterLink} to={process.env.PUBLIC_URL + '/wardrobe'} />
                <Tab label="Outfits" component={RouterLink} to={process.env.PUBLIC_URL + '/outfits'} />
                <Tab label="Styles" component={RouterLink} to={process.env.PUBLIC_URL + '/styles'} />
                <Tab label="About" component={RouterLink} to={process.env.PUBLIC_URL + '/about'} />
              </Tabs>
          )}
        </AppBar>
    );
  }
}

Header.propTypes = {
  user: PropTypes.object,
};

export default Header;