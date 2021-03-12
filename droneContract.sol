pragma ton-solidity >=0.30.0;
pragma AbiHeader pubkey;

contract droneSupply {
    //variable that receives temperature
    uint public temp;
    //variable that receives light intensity 
    uint public lightInt;  
    //variable that receives gps location
    uint8[] public GPSlocation;
    //variable that receives the contract address
    address public droneAddress;
    //variable to store drone password
    string dronePassword;
    //variable to store drone username
    string droneUsername;
    //variable storing public key
    uint256 public m_number;


    struct buyerAgreement{
        string DronePassword;
        string DroneUsername;
    }

    buyerAgreement buyer1_doc;

    constructor() public {
        tvm.accept();

        // Added to facilitate the debugging process
        tvm.log('Constructor');

        temp = 37;
        //droneAddress = address(0xc4a31362f0dd98a8cc9282c2f19358c888dfce460d93adb395fa138d61ae5069);
        lightInt = 10;
        dronePassword = "password";
        //droneAddress = "username";
        //for the gps coordinates example 41°24'12.2"N 2°10'26.5"E, it is arranged in north and south in the array
        GPSlocation = [41,24,12,2,10,26];

        buyer1_doc = buyerAgreement(
            dronePassword,
            droneUsername
        );
    }

        //function sending tons in the network
        function send_grams(address addr, uint64 amount, bool bounce) pure public {
        tvm.accept();
        addr.transfer(amount, bounce);
    }

    onBounce(TvmSlice body) pure external {
        require(body.bits() == 0);
    }


    //Function managing digital signatures
    function setNumber(uint256 value) public {
        require(msg.pubkey() == tvm.pubkey(), 101);
        tvm.accept();
        m_number = value;
    }

    //function to set temperature
        function set_temperature(uint value) public {
        tvm.accept();
        temp = value;
    }


    //function to set contract address
        function set_address(address value) public {
        tvm.accept();
        droneAddress = value;
    }

    //function to set light Intensity
        function set_lightInt(uint value) public {
        tvm.accept();
        lightInt = value;
    }

    //function to set GPS Location

        function set_GPSlocation(uint8[] value) public {
        tvm.accept();
        GPSlocation = value;
    }

    



}