import React from 'react';

const Add = () => {
  const handleAddClick = () => {
    // Get the input element
    const input = document.getElementById('input');

    // Get the input's value
    const value = input.value;

    // Send the value to the server
    socket.emit('add', value);

    // Clear the input
    input.value = '';
  };

  return (
    <button type="submit" id="submit-button" onClick={handleAddClick}>
      Add
    </button>
  );
};

export default Add;
