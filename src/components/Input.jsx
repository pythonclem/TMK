import PropTypes from 'prop-types';
import { FaSearch } from 'react-icons/fa';

const Input = ({ type, label, placeholder, value, onChange }) => {
  return (
    <div className='input-container'>
      <label className='input-container__label'>{label}</label>
      <div className='input-container__input'>
        <input
          type={type}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
        {type === 'search' && <FaSearch />}
      </div>
    </div>
  );
};

Input.propTypes = {
  type: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  placeholder: PropTypes.string,
  value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  onChange: PropTypes.func.isRequired,
};

export default Input;
