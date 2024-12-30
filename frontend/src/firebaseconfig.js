

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCN5yEcyPtsbObW-Pa-i9gTG61JgxqiIH8",
  authDomain: "digital-wardrobe-442615.firebaseapp.com",
  projectId: "digital-wardrobe-442615",
  storageBucket: "digital-wardrobe-442615.firebasestorage.app",
  messagingSenderId: "760879645089",
  appId: "1:760879645089:web:4a90c19b0c338547018be0",
  measurementId: "G-DLV0BPVGMV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export default firebaseConfig;
