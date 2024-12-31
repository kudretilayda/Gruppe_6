import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";


const firebaseconfig = {
  apiKey: "AIzaSyCN5yEcyPtsbObW-Pa-i9gTG61JgxqiIH8",
  authDomain: "digital-wardrobe-442615.firebaseapp.com",
  projectId: "digital-wardrobe-442615",
  storageBucket: "digital-wardrobe-442615.firebasestorage.app",
  messagingSenderId: "760879645089",
  appId: "1:760879645089:web:4a90c19b0c338547018be0",
  measurementId: "G-DLV0BPVGMV"
};

// Initialize Firebase
const app = initializeApp(firebaseconfig);
const auth = getAuth(app);

export { app, auth };
export default class firebaseConfig {
}