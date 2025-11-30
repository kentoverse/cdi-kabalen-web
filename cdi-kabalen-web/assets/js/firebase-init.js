/* Firebase analytics bootstrap for Kabalian CMS builds. */

import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
import { getAnalytics, isSupported } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-analytics.js";

const firebaseConfig = {
  apiKey: "AIzaSyBOQYRrvmRI63wHrO123ouLbHS4_e0cyVg",
  authDomain: "bcbp-can3-cms.firebaseapp.com",
  projectId: "bcbp-can3-cms",
  storageBucket: "bcbp-can3-cms.firebasestorage.app",
  messagingSenderId: "387346958902",
  appId: "1:387346958902:web:1ffa7eee5d68d7ae022697",
  measurementId: "G-WG3TVDS3SM"
};

const app = initializeApp(firebaseConfig);

isSupported()
  .then((supported) => {
    if (!supported) {
      console.warn("Firebase Analytics not supported in this environment.");
      return;
    }
    getAnalytics(app);
  })
  .catch((error) => {
    console.warn("Unable to initialise Firebase Analytics", error);
  });
