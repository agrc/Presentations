import React from 'react';
import Profile from '../Profile';
import profileImage from "../profile.jpg"

export default {
  title: 'Profile',
  component: Profile,
};

const data = {
  firstName: 'Story',
  lastName: 'Book',
  profileImage,
  bio: 'enjoys foraging for food in the rain forest',
  contact: '123-456-7890'
}

export const Empty = () => <Profile />;
export const Normal = () => <Profile {...data} />;
