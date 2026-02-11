import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function HomeScreen() {
  const [message, setMessage] = useState('Connecting to server...');

  useEffect(() => {
    const fetchData = async () => {
      try {
        // IMPORTANT: Replace with your Mac's local IP address
        const response = await fetch('http://192.168.0.135:8000/api/runs/');
        const data = await response.json();

        // Log the data to the terminal for debugging
        console.log('Data fetched from backend:', data);

        // Update the screen to show it worked
        setMessage('Successfully connected to the backend!');

      } catch (error) {
        console.error("Failed to fetch runs:", error);
        setMessage('Failed to connect to the backend.');
      }
    };

    fetchData();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Welcome to VeloCity!</Text>
      <Text style={styles.text}>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 18,
    margin: 10,
  }
});