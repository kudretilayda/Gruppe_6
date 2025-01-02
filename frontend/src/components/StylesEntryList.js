import React, { useState, useEffect } from 'react';
import { Grid, Button, Typography } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import StylesAPI from '../API/StylesAPI';  // API, die die Stile des Kleiderschranks verwaltet
import LoadingProgress from './dialogs/LoadingProgress';
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import StylesEntryCard from './layout/StylesEntryCard';  // Karte, die die einzelnen Stile darstellt

const StylesEntryList = () => {
    const [styles, setStyles] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchStyles();
    }, []);

    // Lädt alle Kleidungsstile
    const fetchStyles = async () => {
        setLoading(true);
        try {
            const fetchedStyles = await StylesAPI.getStyles();
            setStyles(fetchedStyles);
            setLoading(false);
        } catch (err) {
            setError('Fehler beim Laden der Stile');
            setLoading(false);
        }
    };

    const handleAddStyle = () => {
        // Funktion zum Hinzufügen eines neuen Stils, könnte ein Formular öffnen
    };

    if (loading) {
        return <LoadingProgress show={true} />;
    }

    if (error) {
        return <ContextErrorMessage error={error} contextErrorMsg="Fehler beim Laden der Stile" />;
    }

    return (
        <Grid container spacing={2} style={{ padding: 20 }}>
            <Grid item xs={12} style={{ textAlign: 'center' }}>
                <Button
                    variant="contained"
                    color="primary"
                    startIcon={<AddIcon />}
                    onClick={handleAddStyle}
                    sx={{ width: '200px', height: '50px' }}
                >
                    Stil Hinzufügen
                </Button>
            </Grid>
            {styles.length === 0 ? (
                <Typography variant="h6" align="center" style={{ width: '100%' }}>
                    Keine Stile verfügbar
                </Typography>
            ) : (
                styles.map((style) => (
                    <Grid item xs={12} sm={6} md={4} key={style.id}>
                        <StylesEntryCard style={style} />
                    </Grid>
                ))
            )}
        </Grid>
    );
};

export default StylesEntryList;
