import React from 'react'
import { Paper, Typography, Link } from '@mui/material';


function About() {

  return (
    <Paper elevation={0} sx={{ width: '100%', marginTop: 2, marginBottom: 2, padding: 1 }}>
      <div sx={{ margin: 1 }}>
        <Typography variant='h6'>
          Digitaler Kleiderschrank Projekt
        </Typography>
        <br />
        <Typography>
          React Frontend written by Kudret Kilic
        </Typography>
        <Typography>
          Python Backend written by Kudret Kilic
        </Typography>
        <br />
        <Typography variant='body2'>
            Hochschule der Medien 2024
        </Typography>
      </div>
    </Paper>
  )
}

export default About;