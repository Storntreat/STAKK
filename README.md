<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>STAKK</title>
    <link rel="stylesheet" type="text/css" href="stakk.css" />
    <link rel="icon" href="images/NRGlogo.png" type="image/icon" />
  </head>

  <body class="background">
    <!--Heading-->
    <div class="Heading">
      <img
        class="logo"
        src="images/NRGproperlogo.png"
        alt="STAKK logo"
        style="width: 25%; margin-left: 37%"
      />
      <h3 class="centered">
        Teacher Version - Sam&nbsp;Timothy&nbsp;Andy&nbsp;Karikalan&nbsp;Kevin
      </h3>
      <p>
        An extension of TeachAssist, which expands its functionality in
        assisting teachers with student information, assessment and student
        connection. It allows teachers to review students in depth allowing them
        to support and strengthen the needs of each student on a 1-on-1 level
        while being engaging and accessible.
      </p>
    </div>
    <!--Content-->
    <div class="flexcontainer">
      <!--Scrollable box-->
      <div class="scroll">
        <!--list of names that can be clicked-->
        <ul>
          <!--Karikalan Balanayagam-->
          <li>
            <div class="student">
              <img
                src="images/Karkialan Balanayagam.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Balanayagam, Karikalan</p>
                <button
                  class="more-info-button"
                  onclick="show('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Nevin Cui.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Cui, Nevin</p>
                <button
                  class="more-info-button"
                  onclick="show('popup2'); hide('popup1'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Enric Duong.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Duong, Enric</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); show('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>
          <!--student 2-->

          <li>
            <div class="student">
              <img
                src="images/Samuel Lu.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Lu, Samuel</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); show('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Vincent Qu.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Qu, Vincent</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); show('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <!--student 3-->
          <li>
            <div class="student">
              <img
                src="images/Kevin Shen.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Shen, Kevin</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); show('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <!--student 4-->
          <li>
            <div class="student">
              <img
                src="images/Timothy Shnayder.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Shnayder, Timothy</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); show('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Claire Wang.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Wang, Claire</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); show('popup8'); hide('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Josh Wang.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Wang, Joshua</p>
                <button
                  class="more-info-button"
                  onclick="hide('popup1'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); show('popup9'); hide('popup10'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>
          <!--student 5-->
          <li>
            <div class="student">
              <img
                src="images/Andy Zhang.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Zhang, Andy</p>
                <button
                  class="more-info-button"
                  onclick="show('popup10'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup1'); hide('popup9'); hide('popup11');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>

          <li>
            <div class="student">
              <img
                src="images/Dundee Zhang.JPG"
                alt="Student's Picture"
                class="profile-picture"
              />
              <div class="student-info">
                <p>Zhang, Dundee</p>
                <button
                  class="more-info-button"
                  onclick="show('popup11'); hide('popup2'); hide('popup3'); hide('popup4'); hide('popup5'); hide('popup6'); hide('popup7'); hide('popup8'); hide('popup9'); hide('popup10'); hide('popup1');"
                >
                  More Info
                </button>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="vertical-line"></div>
      <!-- Profiles -->
      <div class="popup1" id="popup1" style="display: none">
        <h1 class="centered" id="fullname">Karikalan Balanyagam</h1>
        <img
          class="profilePicture"
          src="images/Karkialan Balanayagam.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup2" id="popup2" style="display: none">
        <h1 class="centered">Nevin Cui</h1>
        <img
          class="profilePicture"
          src="images/Nevin Cui.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup3" id="popup3" style="display: none">
        <h1 class="centered">Enric Duong</h1>
        <img
          class="profilePicture"
          src="images/Enric Duong.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup4" id="popup4" style="display: none">
        <h1 class="centered">Samuel Lu</h1>
        <img
          class="profilePicture"
          src="images/Samuel Lu.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup5" id="popup5" style="display: none">
        <h1 class="centered">Vincent Qu</h1>
        <img
          class="profilePicture"
          src="images/Vincent Qu.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup6" id="popup6" style="display: none">
        <h1 class="centered">Kevin Shen</h1>
        <img
          class="profilePicture"
          src="images/Kevin Shen.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup7" id="popup7" style="display: none">
        <h1 class="centered">Timothy Shnayder</h1>
        <img
          class="profilePicture"
          src="images/Timothy Shnayder.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup8" id="popup8" style="display: none">
        <h1 class="centered">Claire Wang</h1>
        <img
          class="profilePicture"
          src="images/Claire Wang.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup9" id="popup9" style="display: none">
        <h1 class="centered">Joshua Wang</h1>
        <img
          class="profilePicture"
          src="images/Josh Wang.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup10" id="popup10" style="display: none">
        <h1 class="centered">Andy Zhang</h1>
        <img
          class="profilePicture"
          src="images/Andy Zhang.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
      <div class="popup11" id="popup11" style="display: none">
        <h1 class="centered">Dundee Zhang</h1>
        <img
          class="profilePicture"
          src="images/Dundee Zhang.JPG"
          alt="Student's Picture"
        />
        <div>
          <p>Preferred name:</p>
          <p id="preferred"></p>
          <p>Prounouns:</p>
          <p id="pronouns"></p>
          <p>Mark Goal:</p>
          <p id="mark"></p>
          <p>Jobs:</p>
          <p id="jobs"></p>
          <p>Hobbies:</p>
          <p id="hobbies"></p>
          <p>Personality:</p>
          <p id="personality"></p>
          <p>Strengths:</p>
          <p id="strenghts"></p>
          <p>Weaknesses:</p>
          <p id="weaknesses"></p>
          <p>Learning needs:</p>
          <p id="learning"></p>
          <p>Other teacher comments:</p>
          <p id="comments"></p>
        </div>
      </div>
    </div>
    <!-- When clicked, each student's profile shows up-->
    <script>
      $ = function (id) {
        return document.getElementById(id);
      };

      var show = function (id) {
        $(id).style.display = "block";
      };
      var hide = function (id) {
        $(id).style.display = "none";
      };
    </script>
  </body>
</html>
