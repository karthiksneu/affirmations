import React, { useState, useEffect } from 'react';

const Affirmation = () => {
    const [affirmation, setAffirmation] = useState('');
    const [error, setError] = useState('');

    useEffect(() => {
        fetchAffirmation();
    }, []);

    const fetchAffirmation = async () => {
        try {
            const response = await fetch('http://localhost:8000/random-affirmation');
            if (!response.ok) {
                throw new Error('Failed to fetch affirmation');
            }
            const data = await response.json();
            setAffirmation(data.affirmation);
        } catch (error) {
            console.error('Error fetching the affirmation', error);
            setError('Failed to fetch the affirmation');
        }
    };

    return (
        <div>
            <p>✨ {affirmation} ✨</p>
            {error && <p>{error}</p>}
            <button onClick={fetchAffirmation}>Get Another Affirmation</button>
        </div>
    );
};

export default Affirmation;
