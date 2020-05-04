import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders "Recent Posts"', () => {
  const { getByText } = render(<App />);
  const recentPosts = getByText(/Scott Davis/i);
  expect(recentPosts).toBeInTheDocument();
});
