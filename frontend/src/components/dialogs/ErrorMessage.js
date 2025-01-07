import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button, Alert, AlertTitle } from '@mui/material';
import AutorenewIcon from '@mui/icons-material/Autorenew';


class ErrorMessage extends Component {
  #standardText = 'Error: An unexpected error has occurred. Please try again later.';

  render() {
    const { error, ErrorMsg, onReload } = this.props;

    return (
      (error !== null) ?
        <Alert severity='error'>
          <div>
            {this.#standardText}
          </div>
          <AlertTitle>
            {ErrorMsg}
          </AlertTitle>
          <div >
            Error message (for debugging only) is:
          </div>
          <div>
            {error.message}
          </div>
          {
            onReload ?
              <div >
                <Button sx={{ marginTop: 2 }} variant='contained' color='primary' startIcon={<AutorenewIcon />} onClick={onReload}>
                  Reload
                </Button>
              </div>
              : null
          }
        </Alert>
        : null
    );
  }
}


ErrorMessage.propTypes = {

  error: PropTypes.object,

  contextErrorMsg: PropTypes.string,

  onReload: PropTypes.func
}

export default ErrorMessage;