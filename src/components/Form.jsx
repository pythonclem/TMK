import Input from './Input';
import { useState, useEffect } from 'react';
import { CiFootball } from 'react-icons/ci';
import { PiSoccerBallFill } from 'react-icons/pi';
import { FaBasketball } from 'react-icons/fa6';
import { IoIosBaseball } from 'react-icons/io';
import { MdOutlineSportsRugby } from 'react-icons/md';
import { IoTennisball } from 'react-icons/io5';

const Form = () => {
  const [user, setUser] = useState({});
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [teams, setTeams] = useState([
    {
      id: '134221',
      name: 'Alaves',
      altname: 'Deportivo Alavés',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133817',
      name: 'Almeria',
      altname: 'Almería',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133727',
      name: 'Ath Bilbao',
      altname: 'Athletic Bilbao, Athletic Club',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133729',
      name: 'Ath Madrid',
      altname:
        'Atlético de Madrid, Atletico Madrid, Atl. Madrid, Atletico De Madrid',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133739',
      name: 'Barcelona',
      altname: 'FC Barcelona',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133722',
      name: 'Betis',
      altname: 'Real Betis Balompié, Real Betis',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '134222',
      name: 'Cadiz',
      altname: 'Cádiz Club de Fútbol, Cádiz CF',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133937',
      name: 'Celta Vigo',
      altname: 'Celta de Vigo',
      sport: 'Football',
      leagueid: '4335',
    },
    {
      id: '133731',
      name: 'Getafe',
      altname: 'Getafe, Getafe Club de Fútbol',
      sport: 'Football',
      leagueid: '4335',
    },
  ]);
  const [selectedTeams, setSelectedTeams] = useState([]);
  const [filteredTeams, setFilteredTeams] = useState([]);

  const handleTeamSelection = (team) => {
    setSelectedTeams((prevTeams) => [...prevTeams, team]);
  };

  const handleRemoveTeam = (team) => {
    setSelectedTeams((prevTeams) => prevTeams.filter((t) => t !== team));
  };

  const handleSearch = (e) => {
    const input = e.target.value.toLowerCase();
    setSearchInput(input);

    if (input.length > 0) {
      const filtered = teams.filter(
        (team) =>
          (team.name.toLowerCase().includes(input) ||
            team.altname.toLowerCase().includes(input)) &&
          !selectedTeams.includes(team)
      );
      setFilteredTeams(filtered);
    } else {
      setFilteredTeams([]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(user);
  };

  const handleAddTeam = (team) => {
    setSelectedTeams((prevTeams) => [...prevTeams, team]);
    setFilteredTeams([]);
    setSearchInput('');
  };

  const handleRemoveFromSelected = (team) => {
    setSelectedTeams((prevTeams) => prevTeams.filter((t) => t !== team));
  };

  const getAllTeams = async () => {
    try {
      const response = await fetch('');
      const teams = await response.json();
      // Set the teams to the response
    } catch (err) {
      console.log(err);
    }
  };

  const renderIcon = (sport) => {
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

  useEffect(() => {
    const teamIds = selectedTeams.map((team) => team.id);
    setUser({
      name: name,
      email: email,
      teams: teamIds,
    });
  }, [name, email, selectedTeams]);

  return (
    <form className='form' onSubmit={(e) => handleSubmit(e)}>
      <Input
        type='text'
        label='Name'
        placeholder='Enter your name'
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <Input
        type='email'
        label='Email'
        placeholder='myname@example.com'
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <Input
        type='search'
        label='Search'
        placeholder="Start typing your team's name"
        value={searchInput}
        onChange={(e) => handleSearch(e)}
      />
      <div className='search-list'>
        {filteredTeams.map((team) => (
          <div
            className='search-list__item'
            key={team.id}
            onClick={() => handleAddTeam(team)}
          >
            {renderIcon(team.sport.toLowerCase())}
            <p className='search-list__name' key={team.id}>
              {team.name}
            </p>
          </div>
        ))}
      </div>
      <div className='teams-list'>
        {selectedTeams.map((team) => (
          <div className='teams-list__item' key={team.id}>
            <p
              className='btn btn-remove'
              onClick={() => handleRemoveFromSelected(team)}
            >
              x
            </p>
            <p className='teams-list__name'>{team.name}</p>
            {renderIcon(team.sport.toLowerCase())}
          </div>
        ))}
      </div>
      <button className='btn btn-submit' type='submit'>
        Save
      </button>
    </form>
  );
};

export default Form;
