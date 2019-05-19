describe("pow", function() {

    // runs before and after Test.
    before( () => console.log("Test Started"));
    after( () => console.log("Test Finished"));

    // runs before and after each tests.
    beforeEach( () => console.log("individual Test Started"));
    afterEach( () => console.log("individual Testing Finished"));

    describe("x raise to power 3", () => {

      function gen_test(i) {

        let expected = i * i * i;

        it(`${i} raised to power of 3 is ${expected}`, () => {
          assert.equal( pow(i, 3), expected);
        });
      }
  
      for(let x = 0; x <= 8; x++) gen_test(x);
    });

    it("for negative-n it returns NaN", () => {
      assert.isNaN( pow(3, -1));
    });

    it("for Non-Integer n it returns Nan", () => {
      assert.isNaN( pow(3, 1.5));
    });
  
  });

// describe("checkName", function () {

//     it("checks for the valid User", () => {
//       assert.equal(checkName("Harsh"), true);
//     });
// });