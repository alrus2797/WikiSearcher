/* eslint-disable camelcase */
import * as functions from "firebase-functions";
import * as express from "express";
import * as admin from "firebase-admin";
import * as cors from "cors";


admin.initializeApp({
  credential: admin.credential.applicationDefault(),
  databaseURL: "https://wikisearcher-3d8ed-default-rtdb.firebaseio.com",
});

const app = express();
const f = cors({origin: true});
app.use(f);

const db = admin.database();

const pages_ref = db.ref("pages");
const ranks_ref = db.ref("ranks");
const idx_ref = db.ref("indexes");

interface Result {
  url: string,
  rank: number,
  n_coincidences: number
}

app.get("/", async (req, res) => {
  res.status(200).json({message: "Hello Worldadsdasds"});
});

app.get("/search", (req, res)=>{
  if (req.method === "OPTIONS") {
    // Send response to OPTIONS requests
    res.set("Access-Control-Allow-Origin", "*");
    res.set("Access-Control-Allow-Methods", "GET");
    res.set("Access-Control-Allow-Headers", "Content-Type");
    res.set("Access-Control-Max-Age", "3600");
    res.status(204).send("");
  }

  const query = String(req.query.query);
  idx_ref.child(query).once("value", async (data)=>{
    const pids = Object(data.val());
    // console.log("urls fetched", query)
    const urls: Array<Result> = [];
    const idx_requests = Object.keys(pids).map(async (pid)=>{
      return pages_ref.child(pid).once("value", (data)=>{
        const url = data.val();
        return url;
      }).then((data)=>{
        const arg = data.val();
        // console.log('Passed argument', arg)
        return ranks_ref.child(pid).once("value", (data)=>{
          const rank = data.val();
          if (arg !== null) {
            urls.push({url: arg, n_coincidences: pids[pid], rank: rank});
          }
        });
      });
      // let url;
      // await pages_ref.child(pid).once('value', (data)=>{
      //   url = data.val()
      //   console.log("Que fue: ", pid, url)
      //   urls.push(url)
      // }, (err)=>{
      //   url ="F"
      //   console.log("Error fetching: ", err)
      // })
      // return url;
    });

    // const pr_requests = Object.keys(pids).map(async (pid)=>{
    //   return ranks_ref.child(pid).once('value', (data)=>{
    //     let rank = data.val()
    //     if (rank !== null)
    //       ranks.push(rank)
    //   })
    // })

    Promise.all(idx_requests).then(()=>{
      // urls.forEach((element, idx) => {
      //   element.rank = ranks[idx]
      // });
      res.status(200).json({message: urls});
    });
  });
});

exports.app = functions.https.onRequest(app);


// // Start writing Firebase Functions
// // https://firebase.google.com/docs/functions/typescript
//
// export const helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
