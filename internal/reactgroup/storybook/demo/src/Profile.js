import React from "react";

export default function Profile(props) {
  return (
    <div>
      <p className="font-bold text-lg">
        {props.firstName} {props.lastName}
      </p>
      <img className="border rounded-full" src={props.profileImage} alt="profile" />
      <p>{props.bio}</p>
      <p>{props.contact}</p>
    </div>
  );
}
