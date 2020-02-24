import React from 'react';
import propTypes from 'prop-types';

import './AppLogo.css';
import logo from './logo.png';

export function AppLogo({ children: title, className = '', ...restProps }) {
  const classes = `AppLogo ${className}`;
  return (
    <div className={classes} {...restProps}>
      <img src={logo} alt="ITM" title="Logo ITM" />
      {title && <span>{title}</span>}
    </div>
  );
}

AppLogo.propTypes = {
  children: propTypes.string,
  className: propTypes.string,
};
