import React from "react";

export default function Profile(props) {
  const name = `${props.firstName} ${props.lastName}`;

  return (
    <div className="flex border bg-gray-100 border-blue-400 m-6 w-1/2 rounded-lg">
      <div className="flex flex-initial justify-center items-center rounded-l-lg flex-col p-2 bg-white border-r border-blue-400">
        <p className="font-bold text-lg text-gray-700">{name}</p>
        <img className="h-32 border shadow-md rounded-full" src={props.profileImage} alt="profile" />
      </div>
      <div className="flex flex-col self-center ml-5">
        <p>{props.bio}</p>
        <p>{props.contact}</p>
      </div>
    </div>
  );
}
