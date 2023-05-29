import React from 'react';
import axios from 'axios';

function Add() {
  const handleAddReminder = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    const inputField = document.getElementById('reminder-input'); // Get input field data
    const reminderText = inputField.value; // Get value from input field

    try {
        const response = await axios.post('/add-reminder', { reminderText }); // Send POST request to server
        if(response.data.success) {            
            setSuccessMessage('Reminder added successfully'); // Display success message

            setTimeout(() => { // Hide success message after 3 seconds
            setSuccessMessage('');
            }, 3000);

            inputField.value = ''; // Clear the input field after submitting
        } else {
            console.log('Failed to add reminder.'); // Log error message
        }
        

    } catch (error) {
      console.error('Error adding reminder:', error);
    }

  };

  return <button type="submit" onClick={handleAddReminder}>Add</button>;
}

export default Add;







