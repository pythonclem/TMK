import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { renderIcon } from '../helpers/helper';

const TeamList = ({ teams, onRemoveTeam, onReorderTeams }) => {
  const reorder = (list, startIndex, endIndex) => {
    const result = Array.from(list);
    const [removed] = result.splice(startIndex, 1);
    result.splice(endIndex, 0, removed);
    return result;
  };

  const getItemStyle = (isDragging, draggableStyle) => ({
    // some basic styles to make the items look a bit nicer
    userSelect: 'none',

    // change background colour if dragging
    backgroundColor: isDragging && 'rgba(0, 0, 0, 0.1)',
    pointerEvents: 'auto',
    // styles we need to apply on draggables
    ...draggableStyle,
  });

  const Team = ({ team, index }) => (
    <Draggable draggableId={team.id} index={index} key={team.id}>
      {(provided, snapshot) => (
        <div
          className='teams-list__item'
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          style={getItemStyle(
            snapshot.isDragging,
            provided.draggableProps.style
          )}
        >
          <p className='btn btn-remove' onClick={() => onRemoveTeam(team)}>
            x
          </p>
          <p className='teams-list__name'>{team.name}</p>
          {renderIcon(team.sport.toLowerCase())}
        </div>
      )}
    </Draggable>
  );

  const TeamListItems = React.memo(() =>
    teams.map((team, index) => <Team team={team} index={index} key={team.id} />)
  );

  const handleDragEnd = (result) => {
    if (!result.destination) {
      return;
    }

    if (result.destination.index === result.source.index) {
      return;
    }

    const updatedTeams = reorder(
      teams,
      result.source.index,
      result.destination.index
    );

    onReorderTeams(updatedTeams);
  };

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <Droppable droppableId='teamListDroppableId'>
        {(provided) => (
          <div {...provided.droppableProps} ref={provided.innerRef}>
            <TeamListItems />
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  );
};

export default TeamList;
