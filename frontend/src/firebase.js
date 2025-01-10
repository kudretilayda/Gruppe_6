import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import firebaseConfig from './firebaseConfig.js';


//Init Firebase
const app = initializeApp(firebaseConfig);
console.log('Firebase initialized:', app);


export const auth = getAuth(app);
