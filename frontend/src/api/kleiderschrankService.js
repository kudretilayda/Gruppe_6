export const kleiderschrankAPI = {
    getKleidungsstuecke: () => api.get('/kleidungsstuecke'),
    addKleidungsstueck: (data) => api.post('/kleidungsstuecke', data),
    getOutfits: () => api.get('/outfits'),
    createOutfit: (data) => api.post('/outfits', data),
    getStyles: () => api.get('/styles'),
    createStyle: (data) => api.post('/styles', data),
  };
  
  export default api;