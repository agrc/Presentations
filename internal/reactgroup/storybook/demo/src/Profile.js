import React from "react";

export default function Profile(props) {
  const name = `${props.firstName} ${props.lastName}`;

  return (
    <div>
      <p className="font-bold text-lg">{name}</p>
      <img className="h-32 border rounded-full" src={props.profileImage} alt="profile" />
      <p>{props.bio}</p>
      <p>{props.contact}</p>
    </div>
  );
}
