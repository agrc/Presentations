import React, {useState} from "react";
import Profile from "./Profile";
import profileImage from "./monkey.png";

function App(props) {
  const [showProfile, setShowProfile] = useState(false);
  return (<section className="m-4">
    <h1 className="text-5xl">DTS Book</h1>
    <h3 className="text-2xl">Recent Posts</h3>
    <div className="h-20 w-full bg-gray-100 mt-6 p-6 border border-gray-300 rounded">
      <p><span className="text-blue-500 cursor-pointer select-none" onClick={()=> setShowProfile(!showProfile)}>Scott Davis</span>: Good morning!</p>
    </div>
    {showProfile ? <Profile
      firstName="Scott"
      lastName="Davis"
      profileImage={profileImage}
      bio="enjoys foraging for food in the rain forest"
      contact="123-456-7890"
    /> : null}

  </section>);
}

export default App;
