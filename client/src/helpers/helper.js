import { CiFootball } from 'react-icons/ci';
import { PiSoccerBallFill } from 'react-icons/pi';
import { FaBasketball } from 'react-icons/fa6';
import { IoIosBaseball } from 'react-icons/io';
import { MdOutlineSportsRugby } from 'react-icons/md';
import { IoTennisball } from 'react-icons/io5';

export const renderIcon = (sport) => {
  switch (sport) {
    case 'american football':
      return <CiFootball className='teams-list__icon' />;
    case 'football':
      return <PiSoccerBallFill className='teams-list__icon' />;
    case 'basketball':
      return <FaBasketball className='teams-list__icon' />;
    case 'baseball':
      return <IoIosBaseball className='teams-list__icon' />;
    case 'rugby':
      return <MdOutlineSportsRugby className='teams-list__icon' />;
    case 'tennis':
      return <IoTennisball className='teams-list__icon' />;
    default:
      return null;
  }
};
