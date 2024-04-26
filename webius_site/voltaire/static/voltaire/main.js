import * as THREE from 'three'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Scene, camera and renderer setup
 var scene = new THREE.Scene();
 var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
 var renderer = new THREE.WebGLRenderer();
 renderer.setSize(window.innerWidth, window.innerHeight);
 document.body.appendChild(renderer.domElement);

 // Add a light to the scene
 var light = new THREE.PointLight(0xFFFFFF);
 light.position.set(50, 50, 1000);
 scene.add(light);

 // ambient light:
var ambientLight = new THREE.AmbientLight(0xFFFFFF, 0.5); // Color: White, Intensity: 0.5
scene.add(ambientLight);

 // Load GLTF model
 var loader = new GLTFLoader();
 loader.load('/static/voltaire/Voltaire.gltf', function(gltf) {
    var model = gltf.scene;

    // Calculate the center of the model's bounding box
    var boundingBox = new THREE.Box3().setFromObject(model);
    var center = boundingBox.getCenter(new THREE.Vector3());

    // Calculate the distance from the camera to the center of the model
    var distance = boundingBox.getSize(new THREE.Vector3()).length();

    // Set the camera position to be behind the model
    camera.position.copy(center).add(new THREE.Vector3(50, 50, distance));

    // Set the camera's look-at target to the center of the model
    camera.lookAt(center);

    // Add the model to the scene
    scene.add(model);
 }, undefined, function(error) {
     console.error(error);
 });

 // Animation loop
 function animate() {
     requestAnimationFrame(animate);
     renderer.render(scene, camera);
 }
 animate();