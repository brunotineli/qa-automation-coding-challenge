import React from 'react';
import { render, screen, waitFor  } from '@testing-library/react';
import userEvent from '@testing-library/user-event'
import App from './App';

let globalContainer;

describe("App tests", () => {
  describe("Page elements for initial App state", () => {
    beforeEach(() => {
      const { container } = render(<App />);
      globalContainer = container;
    });

    test('Page title', () => {  
      const element = screen.getByText('Get Github Repos');
      expect(element).toBeInTheDocument();
    });
    
    test('Label input', () => {  
      const element = screen.getByLabelText('Github Username');
      expect(element).toBeInTheDocument();
    });
    
    test('Search input', () => { 
      const element = screen.getByRole('textbox', {name: "Github Username"});
      expect(element).toBeInTheDocument();
    });
    
    test('Search button', () => {  
      const element = screen.getByRole('button', {name: "Go"});
      expect(element).toHaveTextContent('Go');
    });

    test('Empty search results', () => {  
      const element = globalContainer.querySelector('.output-status-text');
      expect(element).toHaveTextContent('No repos');
    });
  })

  describe("Search", () => {
    beforeEach(() => {
      const { container } = render(<App />);
      globalContainer = container;
    });

    test('Search when send Enter', async () => {
      await userEvent.type(screen.getByRole('textbox', {name: "Github Username"}), "{enter}")
      expect(globalContainer.querySelector('.circle')).toBeInTheDocument();
    });

    test('Search when click on search button', async () => {
      await userEvent.click(screen.getByRole('button', {name: "Go"}))
      expect(globalContainer.querySelector('.circle')).toBeInTheDocument();
    });

    test('Successful search', async () => {
      await userEvent.type(screen.getByRole('textbox', {name: "Github Username"}), "brunotineli{enter}")
      await waitFor(
        () => expect(screen.getByText(/Found [0-9]+ Repos/i)).toBeInTheDocument(),
        {timeout: 10000}
      );
    });

    test('Not found search', async () => {
      await userEvent.type(screen.getByRole('textbox', {name: "Github Username"}), "{enter}")
      expect(globalContainer.querySelector('.circle')).toBeInTheDocument();
      await waitFor(
        () => expect(screen.getByText('Github user not found')).toBeInTheDocument(),
        {timeout: 10000}
      );
    });
  })
})
