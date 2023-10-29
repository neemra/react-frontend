import React from 'react'
import { useState } from 'react';
// import Image from '../../alheiz (1).jpg'

export default function Portal() {

    const [file, setFile] = useState();
    function handleChange(e) {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    const handleSubmit =()=>{
        //api call
    }
    return (
        <> <div className='container-fluid mt-5'>
            <div className='container mt-5'>
            <div className='row main-frame'>
            
            <div className='col-sm-6 text-center p-3 part1 bg-light'>
                <h2 className=''>Add Image for Detection:</h2>

                <div className="input-group text-center d-flex justify-content-center">
                <div class="btn button btn-file">Choose Image <input onChange={handleChange} type="file"/></div>
                </div>
                
               {file &&( <div className='mt-2'>
                    Uploaded Image 
                <div className='text-center d-flex justify-content-center align-items-center' style={{ width: "100%" }}>
                    <img className='img-fluid w-25 image-border p-2 mt-3' src={file} />
                </div>
                <button className='btn button mt-5' onClick={handleSubmit}>Upload for Detection</button>
                </div>)}

                {!file &&( <div>
                    If you want any further detection and reports First you have to Upload the Image
               
               
                </div>)}
            </div>
            <div className='col-sm-6 part2 text-left p-3'>
                <h1 className='text-left text-light'>Result :</h1>
                <div>Here goes the result of the detection</div>
            </div>
        </div>
        </div>
        </div>
        </>
    )
}
