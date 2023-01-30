# MyRObot
 easyEEZYbotARM on a arduino 
 
 
 Welcome to our demonstration of using a Python and Arduino controller for the EEZYbotARM Mk1 & Mk2 robotic arm. This robotic arm is capable of 3-D kinematics, which allows it to move and manipulate objects in multiple dimensions.

In this demonstration, we will be showing you an algorithm that allows the EEZYbotARM to pick up and move an object to a different position. This functionality can be applied in a variety of industrial settings, such as shipping and logistics, where the ability to accurately and efficiently move items is crucial. We will be explaining the steps of the algorithm and providing visual examples of the robotic arm in action.

Here's an example of how the algorithm could be executed:

•	First, the robotic arm uses its cameras or sensors to locate the object that needs to be picked up. in our case we installed the robot without sensors and gave it the data in advance. this could save costs for the industry 
•	Next, it calculates the best trajectory to reach and grasp the object, taking into consideration any obstacles or constraints in the workspace.
•	Once the arm has securely grasped the object, it uses its 3-D kinematics to calculate the best path to move the object to the desired location, again avoiding obstacles and taking into account any constraints.
•	Finally, the robotic arm releases the object at the desired location.
•	One important aspect to consider when using this algorithm is ensuring that the robotic arm has been properly calibrated, and that its sensors and cameras are working correctly. This will ensure that the arm can accurately locate and manipulate objects. Additionally, safety measures such as obstacle detection and emergency stop systems should be in place to protect both the arm and any individuals working in the vicinity. but in our case we don't have any sensors and we don't have to worry about that.
