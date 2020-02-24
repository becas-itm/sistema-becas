import React from 'react';
import { render } from '@testing-library/react';

import { AppLogo } from './index';

describe('AppLogo component', () => {
  it('renders correctly', () => {
    const { getByTestId } = render(<AppLogo data-testid="logo" />);
    expect(getByTestId('logo')).toBeInTheDocument();
  });

  it('children text should be rendered', () => {
    const { getByTestId } = render(<AppLogo data-testid="logo">foo</AppLogo>);
    expect(getByTestId('logo')).toHaveTextContent('foo');
  });
});
